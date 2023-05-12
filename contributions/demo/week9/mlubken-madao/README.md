# Assignment Proposal

## Title

Multi vs. Single Tenancy - Deploying Single Tenant Applications

## Names and KTH ID
  - Moritz Lübken (mlubken@kth.se)
  - Allan Dao (madao@kth.se)

## Deadline

Week 9

## Category

Demo

## Description

Many well known applications are "multi tenant". That means there is only one "instance" of this application, serving all the users at the same time.
However, especially in the B2B world, there are very good reasons to completely separate the data of your customers.
This can result in a so called single tenant architecture, where every customer (tenant) has their very own instance of your software deployed.

We will look at the differences between single and multi tenant systems, especially the pros and cons.
Then we will demonstrate an example of how to realize a multi tenant system for small scale applications using docker, portainer and a self-built portal to subscribe to applications.

**Relevance**

There are real-world scenarios where deploying single-tenant applications makes a lot of sense. In this case things like licensing/subscriptions management,
automated invoicing etc. become relevant. So far however we didn't look at how this could be achieved. 
