# Assignment Proposal

## Title

Load testing a webservice using wrk

## Names and KTH ID

  - Oliver Schwalbe Lehtihet (oliverle@kth.se)
  - Tao Xiong (taox@kth.se)

## Deadline

- Task 3

## Category

- Executable tutorial

## Description

This tutorial will explain step by step how to Load Test a webservice using the open source CLI tool [wrk](https://github.com/wg/wrk). 

We would start by setting up some simple webservice, like a Flask app. Then installing wrk and going through the usage information. 
Then we would do a simple load test, and finally add a script to the wrk call to e.g. change the URL parameters of every connection that's made in the load test. 

**Relevance**

When hosting a webservice you have to be sure that it can handle the amount of requests that are expected. 
Load testing is an important part of the testing and monitoring process for webservices to ensure there are no downtimes or issues after the app has been deployed. 
