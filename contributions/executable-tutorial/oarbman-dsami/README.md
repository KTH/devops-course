# Assignment Proposal

## Title

**Yappi:** *"the default profiler in PyCharm"*

## Names and KTH ID

- Oscar Arbman (oarbman@kth.se)

- Dania Sami (dsami@kth.se)


## Deadline

- Task 3

## Category

- Executable tutorial

## Description

For the environment, we would use the Killercoda Ubuntu environment. 

We aim to illustrate how to use **Yappi:** *"the default profiler in PyCharm"* to identify which parts of the user's code are slow. This includes working with both normal code and asyncio (concurrent code with async/await). We intend to demonstrate the difference between CPU work and time spent idling or *"wall time"*. Additionally, we will guide the user on how to interpret the results by function and thread. The user should also learn how to start and stop Yappi and how to effectively use this tool.



**Relevance**

Yappi separates Compute vs. Waiting time, enabling the user to find bottlenecks in the code. This is relevant to Week 2 (Continuous Integration), since Yappi can be used during integration to automatically detect performance regressions, ensuring that performance issues are caught early before code is merged.