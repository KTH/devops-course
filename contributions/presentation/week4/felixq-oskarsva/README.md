# Assignment Proposal

## Title
Design patterns for fault tolerance in microservices

## Names and KTH ID
  - Felix Qvarfordt (felixq@kth.se)
  - Oskar Svanström (oskarsva@kth.se)

## Deadline
  - Week 4

## Category
  - Presentation

## Description
Fault tolerance is an important part in a microservice architechture. Since the services often depend on eachother, 
a fault in one can cause a cascading error that halts large parts of the whole system. Therefore, we need to handle faults in different ways to avoid system wide errors. 
Some examples of design patterns that can be used to combat this are the Circuit Breaker Pattern, Bulkhead Pattern, Retry Pattern, Graceful Degradation Pattern etc.

In this presentation, we will go over some of these patterns, when they can be implemented and how they work as well as pros and cons with different patterns.

**Relevance**
Since microservices are becomming more popular and projects generally today are becomming bigger and more complex they need to be tolerat to faults, otherwise they would not be possible.
Microservices themselves are important for DevOps since they enable development processes and deployments to be carried out more independently.
